// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,
  url_api: 'https://platzi-store.herokuapp.com',
  firebase: {
    apiKey: 'AIzaSyD34_g1LVAWJXB2G4l41IbYqH7i4RSFDlw',
    authDomain: 'db-angular-store.firebaseapp.com',
    databaseURL: 'https://db-angular-store.firebaseio.com',
    projectId: 'db-angular-store',
    storageBucket: 'db-angular-store.appspot.com',
    messagingSenderId: '878733621803',
    appId: '1:878733621803:web:459d8decd27d505421c86e'
  }
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.
