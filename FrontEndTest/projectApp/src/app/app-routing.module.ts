import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component'; // Import your components here
import { PlayerDataComponent } from './player-data/player-data.component'; // Import PlayerDataComponent


const routes: Routes = [
  { path: '', component: HomeComponent }, // Define your routes here
  { path: 'players', component: PlayerDataComponent } // Route for player data page

  // Add more routes as needed
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export {routes}
