from nginx:1.19.0

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

# Nginx init
# RUN ["chmod", "+x", "/usr/local/bin/nginx-entrypoint.sh"]
# ENTRYPOINT ["/usr/local/bin/nginx-entrypoint.sh"]
