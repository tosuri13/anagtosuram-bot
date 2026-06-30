.PHONY: deploy bundle

bundle:
	@echo "📦 Bundling Zip Lambda functions..."
	rm -rf dist/shuffle
	uv export --package anagtosuram-bot-app --frozen --no-emit-workspace --no-dev --no-editable -o /tmp/requirements.txt
	uv pip install \
		--no-installer-metadata \
		--no-compile-bytecode \
		--python-platform aarch64-manylinux2014 \
		--python 3.14 \
		--target dist/shuffle \
		-r /tmp/requirements.txt
	cp -r libs/anagtosuram/src/anagtosuram dist/shuffle/anagtosuram
	cp apps/functions/shuffle/function.py dist/shuffle/

deploy: bundle
	@echo "🚀 Deploying CDK stack..."
	cd libs/anagtosuram-cdk && cdk deploy
