set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'DROP DATABASE IF EXISTS task_db'
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'CREATE DATABASE task_db'

PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'DROP TABLE IF EXISTS django_migrations'
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c "DROP TABLE IF EXISTS django_admin_log"
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c "DROP TABLE IF EXISTS django_content_type CASCADE"
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c "DROP TABLE IF EXISTS django_session"
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c "DROP TABLE IF EXISTS auth_permission CASCADE"
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c "DROP TABLE IF EXISTS auth_group CASCADE"
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c "DROP TABLE IF EXISTS auth_group_permissions CASCADE"
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c "DROP TABLE IF EXISTS auth_user CASCADE"
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c "DROP TABLE IF EXISTS auth_user_groups CASCADE"
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c "DROP TABLE IF EXISTS auth_user_user_permissions CASCADE"
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'DROP TABLE IF EXISTS task_tasks'
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'DROP TABLE IF EXISTS task_types'
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'DROP TABLE IF EXISTS tile_status'
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'DROP TABLE IF EXISTS tile_tiles_tasks'
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'DROP TABLE IF EXISTS tiles_tiles'


python manage.py makemigrations task
python manage.py makemigrations tile
python manage.py migrate
python manage.py loaddata */fixtures/*.json
python manage.py createsu
