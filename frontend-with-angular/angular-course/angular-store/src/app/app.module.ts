// Angular
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
// Local
import { FormsModule } from '@angular/forms';

// Angular
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

// Local
//import { CartComponent } from './cart/cart.component';
import { LayoutComponent } from './layout/layout.component';
import { SharedModule } from './shared/shared.module';
import { CoreModule  } from './core/core.module';
// import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    //CartComponent,
    LayoutComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule, // Local
    SharedModule,
    CoreModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
