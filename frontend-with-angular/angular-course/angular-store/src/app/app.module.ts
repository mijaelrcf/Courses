// Angular
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
// Local
import { FormsModule } from '@angular/forms';

// Angular
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
// Local
import { ProductComponent } from './components/product.component';

@NgModule({
  declarations: [
    AppComponent,
    ProductComponent // Local
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule // Local
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
