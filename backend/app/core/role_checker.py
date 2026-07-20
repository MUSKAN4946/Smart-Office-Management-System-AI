from fastapi import Depends, HTTPException, status

from app.core.oauth2 import get_current_user


def admin_required(current_user=Depends(get_current_user)):

    if current_user.role != "Admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Admin can access this API."
        )

    return current_user


def hr_required(current_user=Depends(get_current_user)):

    if current_user.role not in ["Admin", "HR"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only HR or Admin can access this API."
        )

    return current_user


def employee_required(current_user=Depends(get_current_user)):

    if current_user.role not in ["Admin", "HR", "Employee"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access Denied."
        )

    return current_user