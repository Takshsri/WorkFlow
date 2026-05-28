from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.model import Task,User
from schemas.task_schema import TaskCreate,TaskOut, TaskUpdate
from auth import admin_only, get_current_user,manager_only,employee_only

router = APIRouter()

@router.post("/tasks",response_model=TaskOut)
def create_task(task:TaskCreate,
                db:Session = Depends(get_db),
                current_user:User = Depends(manager_only)):
    assigned_user = db.query(User).filter(
        User.id == task.assigned_to
    ).first()

    if not assigned_user:
        raise HTTPException(
            status_code=404,
            detail="Assaigned User not found"
        )
    new_task = Task(
        title = task.title,
        description = task.description,
        priority = task.priority,
        assigned_to = task.assigned_to,
        created_by = current_user.id,
        deadline = task.deadline
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    if current_user.role == "admin":
        tasks = db.query(Task).all() 
    elif  current_user.role == "manager":
        tasks = db.query(Task).filter(
            Task.created_by == current_user.id
        ).all()
    else:
        tasks = db.query(Task).filter(
            Task.assigned_to == current_user.id
        ).all()
    return tasks


@router.get("/tasks/{task_id}")
def get_task(task_id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    task = db.query(Task).filter(
        Task.id == task.id
    ).first()
    if not task:
        raise HTTPException(
            status_code = 404,
            detail="Task not Found"
        )
    return task

@router.patch("/tasks/{task_id}")
def update_task(
    task_id: int,
    updated_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    # EMPLOYEE RULES
    if current_user.role == "employee":

        # employee can update ONLY own tasks
        if task.assigned_to != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="Not authorized"
            )

        # employee can update ONLY status
        if updated_data.status:
            task.status = updated_data.status

        else:
            raise HTTPException(
                status_code=403,
                detail="Employees can update only task status"
            )

    # MANAGER / ADMIN RULES
    else:

        if updated_data.title:
            task.title = updated_data.title

        if updated_data.description:
            task.description = updated_data.description

        if updated_data.priority:
            task.priority = updated_data.priority

        if updated_data.assigned_to:
            task.assigned_to = updated_data.assigned_to

        if updated_data.deadline:
            task.deadline = updated_data.deadline

        if updated_data.status:
            task.status = updated_data.status

    db.commit()

    db.refresh(task)

    return {
        "message": "Task updated successfully",
        "task": task
    }