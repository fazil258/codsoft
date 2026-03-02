FROM jenkins/jenkins:lts

USER root

# Install Docker, Java, Python + venv
RUN apt-get update && \
    apt-get install -y \
        docker.io \
        default-jdk \
        python3 \
        python3-pip \
        python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python3 -m venv /opt/venv

# Set virtual environment path
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements.txt
COPY requirements.txt /opt/requirements.txt

# Install Python dependencies inside venv
RUN pip install --no-cache-dir -r /opt/requirements.txt

# Add jenkins user to docker group
RUN usermod -aG docker jenkins

# Create tasks directory
RUN mkdir -p /home/jenkins/tasks

# Copy task files
COPY Task1.java Task2.py Task4.py /home/jenkins/tasks/

# Compile Java
RUN javac /home/jenkins/tasks/Task1.java

USER jenkins
