import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module'; // Import the routing module if it exists
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    // Declare other components here if needed
  ],
  imports: [
    BrowserModule,
    AppRoutingModule, // Import the AppRoutingModule if you have routing
    // Import other Angular modules and third-party modules here
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }