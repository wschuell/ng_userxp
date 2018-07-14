if [ ! -d ../ng_userxp_deps/naminggamesal ]
then
	cd ..
	mkdir -p ng_userxp_deps
	cd ng_userxp_deps
	git clone https://github.com/flowersteam/naminggamesal.git
	cd naminggamesal
	git checkout develop
	python3 setup.py develop
	cd /code
else
	cd ../ng_userxp_deps/naminggamesal
	git pull
	python3 -c "import naminggamesal" || git checkout develop && python3 setup.py develop
	cd /code
fi;
touch ng/models.py
