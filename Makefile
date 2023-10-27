LEKTOR_FLAGS := scss
BUILD_OUTPUT_PATH ?= ${PWD}/public
BUILD_STATE_PATH ?= ${PWD}/.lektor
SERVER_PORT ?= 8080

server:
	lektor server -f $(LEKTOR_FLAGS) -p $(SERVER_PORT)

clean:
	rm -rf public
	rm -rf assets/static/css

build: clean
	lektor build -f $(LEKTOR_FLAGS) --output-path $(BUILD_OUTPUT_PATH) --buildstate-path $(BUILD_STATE_PATH)
