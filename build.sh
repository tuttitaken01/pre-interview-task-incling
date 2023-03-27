set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'DROP SCHEMA public CASCADE'
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'CREATE SCHEMA public'
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'GRANT ALL ON SCHEMA public TO postgres'
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'GRANT ALL ON SCHEMA public TO public'

PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'DROP DATABASE IF EXISTS task_db'
PGPASSWORD=bE5s7Jt6K7kIW6wTWB0hY9wRm4Bd0oiP psql -U pre_interview_task_user -h dpg-cggr8264daddcg5h9nfg-a pre_interview_task -c 'CREATE DATABASE task_db'


python manage.py makemigrations task
python manage.py makemigrations tile
python manage.py migrate
python manage.py loaddata */fixtures/*.json
python manage.py createsu
