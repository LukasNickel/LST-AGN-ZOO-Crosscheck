CONFIGS := $(shell find configs -mindepth 1 -maxdepth 1 -type d)

all clean: $(CONFIGS)

$(CONFIGS)::
	CONFIG_DIR=$(realpath $@) $(MAKE) -C lst-agn-analysis
