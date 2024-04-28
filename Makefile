LEKTOR_FLAGS := scss
BUILD_OUTPUT_PATH ?= ${PWD}/public
BUILD_STATE_PATH ?= ${PWD}/.lektor
SERVER_PORT ?= 8080

server:
	LEKTOR_DEV=1 lektor server -f $(LEKTOR_FLAGS) -p $(SERVER_PORT)

clean:
	rm -rf public
	rm -rf assets/static/css

build: clean
	lektor build -f $(LEKTOR_FLAGS) --output-path $(BUILD_OUTPUT_PATH) --buildstate-path $(BUILD_STATE_PATH)

new_post:
	mkdir -p content/blog/$(shell date +%Y-%m-%d)-new-post
	echo "title: New post\n---\npub_date: $(shell date +%Y-%m-%d)\n---\nbody:\n\n" >> content/blog/$(shell date +%Y-%m-%d)-new-post/contents.lr
