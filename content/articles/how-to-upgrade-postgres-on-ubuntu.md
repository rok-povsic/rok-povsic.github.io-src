Title: How to upgrade Postgres on Ubuntu 16.04
Date: 2018-07-23 19:25
Category: postgres
Tags: postgres, upgrade
Authors: Rok Povšič

This is a guide on how to upgrade Postgres. The commands below will install a new Postgres 9.6 instance, migrate all the data, and afterwards uninstall the old Postgres 9.5 instance.

> Note: I've used these exact commands on Ubuntu 16.04. Your mileage may vary on other OSes and Postgres versions.

### 1. Install the new version

```python
sudo apt-get install postgresql-9.6
```

### 2. Make sure both version are installed and running

```python
sudo pg_lsclusters
```

The output should be something like:

```python
Ver Cluster Port Status Owner    Data directory               Log file
9.5 main    5432 online postgres /var/lib/postgresql/9.5/main /var/log/postgresql/postgresql-9.5-main.log
9.6 main    5433 online postgres /var/lib/postgresql/9.6/main /var/log/postgresql/postgresql-9.6-main.log
```

### 3. Migrate the data from old to new

Your ports may be different, check the previous command's output.

```python
sudo -u postgres -i
pg_dumpall -p 5432 | psql -d postgres -p 5433
exit
```

### 4. Update the ports

Open `postgresql.conf` and set the `port` value of the 9.6 instance in to 5432. If you're going to keep the 9.5 version, also set its port to some other integer (e.g. 5433).

```python
sudo vim /etc/postgresql/9.5/main/postgresql.conf
sudo vim /etc/postgresql/9.6/main/postgresql.conf
```

### 5. Uninstall the old version (optional)

```python
sudo apt-get purge postgresql-9.5
```

### 6. Ensure the new version is up

Make sure the port is set correctly.

```python
sudo service postgresql start
sudo pg_lsclusters
```