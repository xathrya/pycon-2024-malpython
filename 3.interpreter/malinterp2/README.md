# Malicious Interpreter Example 

This sample is used to demonstrate common tricks by threat actor to masquerade malicious code.

We will patch the python, specifically [Python 3.11.9](https://www.python.org/downloads/release/python-3119/), and insert our payload.

## Malinterp 2: Run Payload on New Thread

This sample will execute attacker payload on new thread. Specifically, we will initiate reverse shell to attacker-controlled server. The server information (IP and port) is hardcoded as `IP=127.0.0.1` and `port=4444`

Note: this sample use pthread to create new thread and most likely run on unix only.

## Preparation

We have diff file that will be patched into the source code. First we need to extract the source code and then apply the patch. If you want to apply patch in other sample, make sure to undo the patch.

```sh
mkdir /tmp/workdir 
pushd /tmp/workdir

# get the source code
wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tar.xz

# extract the python source code 
tar -xf Python-3.11.9.tar.xz
mv Python-3.11.9 base

popd
```

## Build

Patch the source code using the `file.patch`

```sh
# copy the file.patch to the same folder as the source code.
cp file.patch /tmp/workdir
pushd /tmp/workdir

# apply the patch
patch -s -p0 < file.patch

# build the executable
cd base
./configure
make

popd
```

## Execute

As this sample will initiate connection to our server, we need to prepare server that should listen on `127.0.0.1:4444`. To simulate this, we only need `nc`.

```sh
# on linux
nc -nlvp 4444

# on macos (BSD)
nc -l 4444
```

Then, execute our python executable. Make sure you are in source tree or python root directory.

## Undo Patch

If you want to apply patch in other sample using the same source tree, then make sure to undo the patch. To remove or undo the patch do following.

```sh
# undo the patch
patch -R -p0 < file.patch
```