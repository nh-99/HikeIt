#!/usr/bin/env bash
ln -s /vagrant/* /home/vagrant/

apt-get update

debconf-set-selections <<< 'mysql-server mysql-server/root_password password foobar'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password foobar'
apt-get install -y mysql-server

apt-get install -y mysql-client
apt-get install -y libmysqlclient-dev
apt-get install -y python
apt-get install -y python-dev
apt-get install -y python-pip

pip install -r /vagrant/requirements.txt
chmod +x /vagrant/manage.py

if grep -Fxq "export HIKEIT_DB_USER" /home/vagrant/.profile
then
echo "User already exists"
else
echo "export HIKEIT_DB_USER='root'" >> /home/vagrant/.profile
fi

if grep -Fxq "export HIKEIT_DB_PASSWORD" /home/vagrant/.profile
then
echo "User already exists"
else
echo "export HIKEIT_DB_PASSWORD='foobar'" >> /home/vagrant/.profile
fi

mysql -u root --password=writwritwrit -e 'create database hikeit_dev;'

su -c "source ~/.profile; python /vagrant/manage.py migrate" vagrant

