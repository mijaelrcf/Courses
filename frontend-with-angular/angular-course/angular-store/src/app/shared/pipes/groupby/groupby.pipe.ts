import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'groupby'
})
export class GroupbyPipe implements PipeTransform {

  transform(productSelected: any, products: any[]): any {
    return products.filter((product) => productSelected.id === product.id).length;
   }
}
