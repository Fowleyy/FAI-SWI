import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

// Ionic standalone komponenty, které používáš v HTML
import {
  IonHeader, IonToolbar, IonTitle, IonContent,
  IonButton, IonItem, IonLabel, IonInput,
  IonList, IonListHeader, IonIcon
} from '@ionic/angular/standalone';

@Component({
  selector: 'app-tab1',
  standalone: true,                           // DŮLEŽITÉ
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss'],
  imports: [
    CommonModule, FormsModule,                // pro *ngIf, *ngFor, [(ngModel)]
    IonHeader, IonToolbar, IonTitle, IonContent,
    IonButton, IonItem, IonLabel, IonInput,
    IonList, IonListHeader, IonIcon
  ],
})
export class Tab1Page {
  count = 0;
  itemName = '';
  savedItems: { name: string; value: number }[] = [];

  onIncrement() { this.count++; }             // opravený název (volání v HTML také uprav)
  onReset() { this.count = 0; }
  onSave() {
    if (!this.itemName.trim()) return;
    this.savedItems.push({ name: this.itemName.trim(), value: this.count });
    this.itemName = '';
    this.count = 0;
  }
  onDelete(i: number) { this.savedItems.splice(i, 1); }
}