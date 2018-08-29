

FILE=ngal_branch.txt
if [ -f $FILE ]; then
   NGALBRANCH=$(cat $FILE)
else
   NGALBRANCH=nguser_xp
   echo $NGALBRANCH>$FILE
fi

echo "NGALBRANCH:"$NGALBRANCH

pip install cython
if [ ! -d ../ng_userxp_deps/naminggamesal ]
then
	(cd .. &&
	mkdir -p ng_userxp_deps &&
	cd ng_userxp_deps &&
	git clone https://github.com/flowersteam/naminggamesal.git &&
	cd naminggamesal &&
	git checkout $NGALBRANCH &&
	python3 setup.py develop) || exit 1
	# cd /code
elif [ ! "$1" == "installonly" ]
then
	(cd ../ng_userxp_deps/naminggamesal &&
	git pull &&
	git checkout $NGALBRANCH &&
	python3 setup.py develop) || exit 1
	#cd /code
else
	(cd ../ng_userxp_deps/naminggamesal &&
	git checkout $NGALBRANCH ) || exit 1
fi;
touch ng/models.py
