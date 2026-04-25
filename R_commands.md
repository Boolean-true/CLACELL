# R commands in the command line

## Setup in Arch Linux

```console
mkdir -p ~/R/library
```

## Install package

```console
Rscript -e ".libPaths('~/R/library'); install.packages(c('hdf5r', 'metap', 'mutoss'), repos='https://cloud.r-project.org/', lib='~/R/library')"
```

```console
Rscript -e ".libPaths('~/R/library'); install.packages(c('hdf5r', 'metap', 'mutoss'), repos='https://cloud.r-project.org/', lib='~/R/library')"
```

## Execute script

```console
Rscript -e ".libPaths('~/R/library'); rio::convert('human_pbmc_marker.rda', 'human_pbmc_marker.json')"
```
