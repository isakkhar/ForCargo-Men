#!/usr/bin/env sh

# Set parameters
owner='root'
#group='wheel'
group='sveta'
dmod='755'
fmod='644'
psqluser='pgsql'
psqlrole='sveta'

# We are going to copy from current directory, parent might be used too
srcdir=`pwd`
psdir=${srcdir%/*}
hstnm=`hostname`

# Set up the destination directory with no trailing '/'
if [ $# = 0 ]; then
  dstdir='.'
elif [ $# = 1 ]; then
  dstdir=$1
  if [ $dstdir = ${dstdir#/} ]; then
    echo "Destination should be absolute path starting with /."
    exit 1
  fi
  # Remove trailing / if any
  dstdir=${dstdir%/}
else
  echo "Usage: cd source ; ./install.sh [destination]"
  exit 1
fi
if [ $srcdir = $dstdir ]; then
  dstdir='.'
fi

# Set up destination parent
if [ $dstdir != '.' ]; then
  pddir=${dstdir%/*}
else
  pddir=$psdir
  sedcom=" -e s/DEBUG=False/DEBUG=True/"
fi

sedcom=" -e s,localhost,$hstnm,"$sedcom

sedcommand="sed -e s,__PROJECTROOT__,$pddir,"$sedcom

# Bail out on wrong dir name
if [ $srcdir = $psdir/django-logistics ] && [ $dstdir = '.' ]; then
  echo "Rename $psdir/django-logistics to $psdir/django_logistics"
  exit 1
fi

echo "Source: $srcdir, parent: $psdir. Destination: $dstdir, parent: $pddir"

rm -f $dstdir/settings.py
#sed -e "s,__PROJECTROOT__,$pddir," < settings.py.in > settings.py
$sedcommand < settings.py.in > settings.py

if [ $dstdir != '.' ]; then
  grep -v '^#' dirlist | sed "s,^,$dstdir/," | xargs install -o $owner -g $group -m $dmod -d
  for ii in `grep -v '^#' fillist` settings.py ; do
    install -o $owner -g $group -m $fmod $ii $dstdir/$ii
  done
  cd $dstdir
fi

#sed -e s,HSTNM,$hstnm,g < site.sql | psql fishtrip
#cat site.sql | sed -e s,HSTNM,$hstnm,g | psql fishtrip

django-admin.py compilemessages
