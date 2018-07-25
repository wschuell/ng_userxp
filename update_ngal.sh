# if not set NGALBRANCH and no file set to develop and write in config file
# if not set and file get from file
if [ ! -d ../ng_userxp_deps/naminggamesal ]
then
	cd ..
	mkdir -p ng_userxp_deps
	cd ng_userxp_deps
	git clone https://github.com/flowersteam/naminggamesal.git
	cd naminggamesal
	git checkout $NGALBRANCH
	python3 setup.py develop
	cd /code
else
	cd ../ng_userxp_deps/naminggamesal
	git pull
	python3 setup.py develop
	cd /code
fi;
touch ng/models.py
