FROM jenkins/jenkins:lts

USER root

# Install required tools only
RUN apt-get update && \
    apt-get install -y \
        default-jdk \
        python3 \
        python3-pip \
        python3-venv \
        curl \
        ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Docker CLI manually (lighter & safer)
RUN curl -fsSL https://get.docker.com | sh

# Create virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements
COPY requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir -r /opt/requirements.txt

# Add jenkins user to docker group
RUN usermod -aG docker jenkins

# Create tasks folder
RUN mkdir -p /home/jenkins/tasks

# Copy task files
COPY Task1.java Task2.py Task4.py /home/jenkins/tasks/

# Compile Java
RUN javac /home/jenkins/tasks/Task1.java

USER jenkins
