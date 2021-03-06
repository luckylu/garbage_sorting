from fabric import task,Connection
# from invoke import Responder
# from ._credentials import github_username, github_password


# def _get_github_auth_responders():
#     """
#     返回 GitHub 用户名密码自动填充器
#     """
#     username_responder = Responder(
#         pattern="Username for 'https://github.com':",
#         response='{}\n'.format(github_username)
#     )
#     password_responder = Responder(
#         pattern="Password for 'https://{}@github.com':".format(github_username),
#         response='{}\n'.format(github_password)
#     )
    # return [username_responder, password_responder]
@task()
def deploy(c):
    supervisor_conf_path = '/etc/'
    supervisor_program_name = 'garbage'

    project_root_path = '~/www/garbage_sorting/'
    frontend_path = project_root_path + '/frontend'
    # 先停止应用
    with c.cd(supervisor_conf_path):
        cmd = '/home/michael/.local/bin/supervisorctl stop {}'.format(supervisor_program_name)
        c.run(cmd)

    # 进入项目根目录，从 Git 拉取最新代码
    with c.cd(project_root_path):
        cmd = 'git pull'
        # responders = _get_github_auth_responders()
        c.run(cmd)

    # build vue
    with c.cd(frontend_path):
        cmd = '/usr/bin/yarn build'
        c.run(cmd)


    # 安装依赖，迁移数据库，收集静态文件
    with c.cd(project_root_path):
        c.run('/home/michael/.local/bin/pipenv install --deploy --ignore-pipfile')
        c.run('/home/michael/.local/bin/pipenv run python manage.py migrate')
        c.run('/home/michael/.local/bin/pipenv run python manage.py collectstatic --noinput')

    # 重新启动应用
    with c.cd(supervisor_conf_path):
        cmd = '/home/michael/.local/bin/supervisorctl start {}'.format(supervisor_program_name)
        c.run(cmd)
