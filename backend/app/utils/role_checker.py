from fastapi import Depends, HTTPException, status

from app.api.user_api import get_current_user


def admin_required(current_user=Depends(get_current_user)):

    if current_user.role != "Admin":

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Admin Can Access This Resource"
        )

    return current_user