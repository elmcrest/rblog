from fabric.api import cd, env, get, lcd, local, prefix, run, sudo

env.hosts = ["metal.raesener.de"]


def create_container():
    "create the rblog container locally and upload to docker repo"
    local("python manage.py compilecss")
    local("docker-compose build app")
    local("docker push elmcrest/rblog")
    with cd("rblog"):
        run("docker-compose stop app")
        run("docker-compose pull elmcrest/rblog")
        run("docker-compose up -d app")
