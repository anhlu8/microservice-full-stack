validata-circleci:
	circleci config process .circleci/config.yml

run-circleci-local:
	circleci local execute