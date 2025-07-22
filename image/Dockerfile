From public.ecr.aws/lambda/python:3.10

# install Requirements
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt

COPY src/* ${LAMBDA_TASK_ROOT}

CMD ["main.handler"]



# FROM public.ecr.aws/lambda/python:3.10

# WORKDIR /app

# COPY requirements.txt ${LAMBDA_TASK_ROOT}
# RUN pip install --no-cache-dir -r requirements.txt

# COPY ./src ${LAMBDA_TASK_ROOT}

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]