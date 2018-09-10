.PHONY: all test static
all:
	bash bin/runserver.sh

test:
	bash bin/test.sh

static:
	bash bin/collectstatic.sh
