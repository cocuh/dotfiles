if [ -e ~/.python/startup.py ];then
    export PYTHONSTARTUP=~/.python/startup.py
fi
for vwpath in $(where virtualenvwrapper.sh);do
    if [ -e $vwpath ];then
        source $vwpath
    fi
done

install_jupyter_in_virtualenv() {
    pip install ipykernel
    version=$(python -c 'import sys;print(sys.version[0])')
    vname=$(basename ${VIRTUAL_ENV})
    python -m ipykernel install --user --name="python${version}-${vname}"
}


