#!/bin/bash

# exit if fail
function eif {
    "$@"
    if [[ $? -ne 0 ]]; then
        echo "Error at: $@"
        exit 1
    fi
}

DOMAIN=school.com

eif cp -r ./static /var/www/
eif chown www-data:www-data -R /var/www/static/

eif cp -r ./virtual-env /var/www/
eif chown www-data:www-data -R /var/www/virtual-env/

eif cp -r ./school /var/www/
eif sed -i "s/DEBUG = True/DEBUG = False/g" \
    /var/www/school/school/settings.py
eif sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \['$DOMAIN'\]/g" \
    /var/www/school/school/settings.py
eif chown www-data:www-data -R /var/www/school/

eif cp ./deploy/django.conf /etc/apache2/sites-available
eif a2ensite django

eif apachectl restart
