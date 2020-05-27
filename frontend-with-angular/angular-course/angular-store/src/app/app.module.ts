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
import { CartComponent } from './cart/cart.component';
import { ExponentialPipe } from './exponential.pipe';

@NgModule({
  declarations: [
    AppComponent,
    ProductComponent,
    CartComponent,
    ExponentialPipe // Local
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
