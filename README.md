## Dockerised Airflow v.2.10.3

This repo contains setup files that should allow you to run a Dockerised version of Airflow 2.10.3
The setup has been tested on Windows 10 and Debian Linux (I'm on Kali, other Debian distros should work as well).


# Prerequisites

You will need `docker` and `docker-compose`.

On Windows you can get both by installing [**Docker Desktop**](https://docs.docker.com/desktop/setup/install/windows-install/).

On Debian [**these**](https://docs.docker.com/engine/install/debian/) instructions should work.

**N.B.** Docker Desktop is much, much more resource hungry than the binaries.

# How to run

On either platform, `cd` into the root folder (i.e. this folder, where the `docker-compose.yml` file is). Execute:

    docker compose up airflow-init

Wait for the script to do its thing. It has finished when it gives you the commandline back. Then execute:

    docker compose up

It won't give you the comand line back. Once you see `airflow-scheduler`, `airflow-worker` and `airflow-webserver` spawning messages, try to open front-end on `http://localhost:8088`. It may take a while, if there are no obvious errors in the console, give it more time.

**Username/Password:** *airflow/airflow*

**N.B.** I used non-default port 8088, because I already had Jenkins on 8080. But you can use any port, simply find-and-replace in the `docker-compose.yml` file.

# Notes on Debian

Everything from this point forward is terrible idea from security point of view, it's a quick and very dirty, short term(!!) solution. You have been warned.

1. The above `docker compose` commands won't work unless you [configure a user-group](https://medium.com/devops-technical-notes-and-manuals/how-to-run-docker-commands-without-sudo-28019814198f#:~:text=By%20default%20that%20Unix%20socket,and%20add%20users%20to%20it.) for it. But you can run the commands with `sudo` instead.

2. You need to make sure that whatever user you start the docker with has `rwe` access to the `./dags` folder. If you started docker with `sudo`, you can give access to all users to do whatever they want in the `./dags` folder by executing:
    
        sudo chmod -R 777 dags


