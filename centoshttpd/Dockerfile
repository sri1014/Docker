FROM centos:7
RUN yum -y update
RUN yum install -y httpd
COPY index.html /var/www/html
EXPOSe 80
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
