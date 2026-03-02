FROM jenkins/jenkins:lts

USER root

# Install Docker CLI properly
RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get clean

# Install Java (for Task1.java)
RUN apt-get update && \
    apt-get install -y default-jdk && \
    apt-get clean

# Install Python3 (for Task2.py, Task4.py)
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean
    
# Copy requirements.txt into the image
COPY requirements.txt /opt/requirements.txt

# Install Python dependencies
RUN pip3 install --no-cache-dir -r /opt/requirements.txt

# Add jenkins user to docker group
RUN usermod -aG docker jenkins

# Create directory for tasks
RUN mkdir -p /home/jenkins/tasks
COPY Task1.java Task2.py Task4.py /home/jenkins/tasks/

# Compile and run Java + run Python tasks
# (This runs when building the image — remove if you want Jenkins to run them instead)
RUN javac /home/jenkins/tasks/Task1.java

# Optional: Run the tasks during build (comment out if not needed)
# RUN java -cp /home/jenkins/tasks Task1
# RUN python3 /home/jenkins/tasks/Task2.py
# RUN python3 /home/jenkins/tasks/Task4.py

USER jenkins


