import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClient, HttpClientModule } from '@angular/common/http'; // Import HttpClientModule
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PlayerDataComponent } from './player-data/player-data.component'; // Import PlayerDataComponent if not imported
import { PlayerService } from './player.service';


@NgModule({
  declarations: [
    AppComponent,
    PlayerDataComponent // If not already imported
  ],
  imports: [
    BrowserModule,
    HttpClientModule, // Add HttpClientModule here
    AppRoutingModule
  ],
  providers: [PlayerService, HttpClient],
  bootstrap: [AppComponent]
})
export class AppModule { }
