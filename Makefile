FUNCTIONS := $(notdir $(wildcard apps/functions/*))

.PHONY: deploy destroy bundle requirements $(addprefix bundle-,$(FUNCTIONS))

requirements:
	@echo "📦 Exporting requirements..."
	mkdir -p dist
	uv export --package anagtosuram-bot-app --frozen --no-emit-workspace --no-dev --no-editable -o dist/requirements.txt

bundle: $(addprefix bundle-,$(FUNCTIONS))

$(addprefix bundle-,$(FUNCTIONS)): bundle-%: requirements
	@echo "📦 Bundling $*..."
	rm -rf dist/$*
	uv pip install \
		--no-installer-metadata \
		--no-compile-bytecode \
		--python-platform aarch64-manylinux2014 \
		--python 3.14 \
		--target dist/$* \
		-r dist/requirements.txt
	cp -r libs/anagtosuram/src/anagtosuram dist/$*/anagtosuram
	cp -r apps/functions/$*/. dist/$*/

deploy: bundle
	@echo "🚀 Deploying CDK stack..."
	cd libs/anagtosuram-cdk && cdk deploy

destroy: bundle
	@echo "🔥 Destroying CDK stack..."
	cd libs/anagtosuram-cdk && cdk destroy
