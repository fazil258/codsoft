FROM jenkins/jenkins:lts

USER root

# Install Docker, Java, Python
RUN apt-get update && \
    apt-get install -y \
        docker.io \
        default-jdk \
        python3 \
        python3-pip && \
    apt-get clean

# Copy requirements.txt
COPY requirements.txt /opt/requirements.txt

# Install Python dependencies
RUN pip3 install --no-cache-dir -r /opt/requirements.txt

# Add jenkins user to docker group
RUN usermod -aG docker jenkins

# Create tasks directory
RUN mkdir -p /home/jenkins/tasks

# Copy task files
COPY Task1.java Task2.py Task4.py /home/jenkins/tasks/

# Compile Java (optional)
RUN javac /home/jenkins/tasks/Task1.java

# Optional: Do NOT run tasks inside Docker build
# RUN java -cp /home/jenkins/tasks Task1
# RUN python3 /home/jenkins/tasks/Task2.py
# RUN python3 /home/jenkins/tasks/Task4.py

USER jenkins
