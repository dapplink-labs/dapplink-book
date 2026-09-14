FROM nginx:alpine

COPY index.html /usr/share/nginx/html/
COPY assets/ /usr/share/nginx/html/assets/
COPY assets/logos/dapplink.png /usr/share/nginx/html/favicon.ico
COPY DappLink_Book.pdf /usr/share/nginx/html/

EXPOSE 80

