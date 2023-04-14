# Notes

## Process
Following the tutorial for djangorestframework

## Issues
1. `make django` does not work
```
Preparing transaction: done                                                                                                                                                  
Verifying transaction: done                                                                                                                                                  
Executing transaction: done                                                                                                                                                  
cd templates/django && django-admin startproject example \                                                                                                                   
&& cd example && python manage.py runserver                                                                                                                                  
CommandError: '/workspace/anaconda-eats/templates/django/example' already exists                                                                                             
make: *** [Makefile:13: django] Error 1     
```

1. If you open gitpod as in the instructions, the upstream repo will be anaconda-interviews/anaconda-eats, not the fork. Might be worth mentioning.

1. You probably want to write-protect against creating new branches there