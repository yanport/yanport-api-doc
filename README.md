## Contributing

Thank you for investing your time in contributing to our project! Any contribution you make will be reflected [here](https://www.yanport.com/donnees-immobilieres/api/documentation) :sparkles:.

### Pull Request Process

1. Fork the Yanport-api-doc repository and commit your changes.
   
2. When you're finished with the changes, create a pull request.

3. (Optional) We may ask for changes to be made before a PR can be merged, either using suggested changes or pull request comments. Please apply the suggested changes and commit them to your branch.
   
4.  Once a maintainer approve the pull request, he will take care of merging the pull request.

### Your PR is merged!

Congratulations :tada::tada: The Yanport team thanks you :sparkles:. 

## Testing
1. Generate documentation
```shell
npx @redocly/cli@1.34.5  bundle src/openapi.yaml -o dist/openapi.yaml
```
2. Check changes, for example with [https://editor.swagger.io](https://editor.swagger.io)
