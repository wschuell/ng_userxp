

FILE=ngal_branch.txt
if [ -f $FILE ]; then
   NGALBRANCH=$(cat $FILE)
else
   NGALBRANCH=develop
   echo $NGALBRANCH>$FILE
fi

echo "NGALBRANCH:"$NGALBRANCH

pip install cython
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
	git checkout $NGALBRANCH
	python3 setup.py develop
	cd /code
fi;
touch ng/models.py
