# DASHBOARD

### **Update maps**
```
use [Yed Graph Editor](http://www.yworks.com/products/yed) tools to edit view\assets\images\envs\*.graphml

export .graphml to view/src/assets/images/envs/*.svg
	Clipping/Scaling Factor : 0.7
	Links and description/Open link in New Windows (unselected)

```

### **Update view folder**

First, you should be familiar with **Vue.js** or other similar frameworks (Angular2, React, Polymer, etc...).

Vue.js is simple and easy to learn :

Follow this tutorial : [Getting started Vue.js](https://vuejs.org/v2/guide/)

Make sure you understand the following concepts :

* node.js  (server side running javascript using ChromeV8 engine)
* npm (node package manager to install node.js modules)
* webpack
* vue-router
* vue-cli (https://www.npmjs.com/package/vue-cli)

### View Architecture

**Vue-cli** offers commands to quickly generate new projects from templates.

https://github.com/vuejs-templates

The **view folder** architecture is a mix between the **webpack-simple template** and **webpack template**

First we create the project using the **webpack-simple template**.

We integrate some architecture ideas from **webpack template** to make the architecture most understandable.

Be aware that the default **webpack template** from **vue-cli** is quite complex.

We can say that the **current architecture** is a custom version of the **webpack template**.

Take a close look at the **webpack.config.js** file and notice that we configure an alias  ``` @ ``` that point to the ``` src ``` folder.

We also configure a resolve mechanism so we do not need to sepcify the file extension during imports.

```
resolve: {
		extensions: ['.js', '.vue', '.json', '.svg'],
		alias: {
			'vue$': 'vue/dist/vue.esm.js',
			'@': resolve('src'),
		}
    
```

### **Install dependencies**

Download  and Install :

 * node.js 
 * npm

Change directory to **view directory** 

```$ cd view ```

Install dependencies (node.js and npm should be installed first)

```$ npm install ```

By running this command npm will locate **package.json** file and install all the dependencies and devDependencies in this file.

If you do not have access to internet use the following internal registry : 

```$  npm install --registry https://artifactory-iva.si.francetelecom.fr/artifactory/api/npm/npmproxy/   ```

### **Run localy, dev mode**

```$ npm run dev ```

The following script located in package.json is executed

```   
"scripts": {
    "dev": "cross-env NODE_ENV=development webpack-dev-server --open --hot"
  }

```

A local server will be available on localhost

```
http://localhost:8080

```

### **Package and deploy**

```$ npm run build ```

The following script located in package.json is executed

```

"scripts": {
    "build": "cross-env NODE_ENV=production webpack --progress --hide-modules"
  }

```
The script will parse the application and build **html/css/js** in folder **view/build/** for production with minification.

Do not forget to push on remote git repository

```$ git push ```








