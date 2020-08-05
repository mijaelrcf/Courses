import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'deleteRepeats'
})
export class DeleteRepeatsPipe implements PipeTransform {

  transform(products: any, ...args: any[]): any {
    console.log('deleteRepeats');
    console.log(products);
    return ([...new Set(products)]);
  }

}
