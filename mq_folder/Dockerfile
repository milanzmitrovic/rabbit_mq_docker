
FROM rabbitmq:3.8-management-alpine

ENV RABBITMQ_DEFAULT_USER=myuser
ENV RABBITMQ_DEFAULT_PASS=mypassword


# Expose is used to enable communication between containers within same network
# When mapping ports on command line using -p, expose ports will be overriden
EXPOSE 5672
EXPOSE 15672


