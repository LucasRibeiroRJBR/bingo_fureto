import flet as ft
from random import randint

sorteados = []

nums = []
while len(nums) != 25:
    x = randint(0,100)
    if x not in nums:
        nums.append(x)
    

class Cartela(ft.UserControl):
    def __init__(self,n):
        super().__init__()
        self.n = n

    def build(self):
        self.c1 = ft.Container(
            ft.Text(self.n, style=ft.TextThemeStyle.DISPLAY_MEDIUM,color=ft.colors.WHITE),
            alignment=ft.alignment.center,
            width=60,
            height=60,
            border_radius=8,
            bgcolor=ft.colors.BLUE_GREY_500
        )

        return self.c1

def main(page:ft.Page):
    page.title='teste'

    def sortear(e):
        while x != sorteados:
            x = randint(0,100)
            sorteados.append(x)
            print(sorteados,x)
            break

    bt_sortear = ft.TextButton(content=ft.Container(
                                    content=ft.Column([
                                        ft.Text(value='Sortear',size=50)
                                    ]
                                )
                            ),on_click=sortear)

    page.add(ft.Row([Cartela(n=nums[0]),Cartela(n=nums[1]),Cartela(n=nums[2]),Cartela(n=nums[3]),Cartela(n=nums[4])],ft.MainAxisAlignment.SPACE_AROUND),
             ft.Row([Cartela(n=nums[5]),Cartela(n=nums[6]),Cartela(n=nums[7]),Cartela(n=nums[8]),Cartela(n=nums[9])],ft.MainAxisAlignment.SPACE_AROUND),
             ft.Row([Cartela(n=nums[10]),Cartela(n=nums[11]),Cartela(n=nums[12]),Cartela(n=nums[13]),Cartela(n=nums[14])],ft.MainAxisAlignment.SPACE_AROUND),
             ft.Row([Cartela(n=nums[15]),Cartela(n=nums[16]),Cartela(n=nums[17]),Cartela(n=nums[18]),Cartela(n=nums[19])],ft.MainAxisAlignment.SPACE_AROUND),
             ft.Row([Cartela(n=nums[20]),Cartela(n=nums[21]),Cartela(n=nums[22]),Cartela(n=nums[23]),Cartela(n=nums[24])],ft.MainAxisAlignment.SPACE_AROUND),
             ft.Row([bt_sortear],ft.MainAxisAlignment.SPACE_AROUND))
    page.update()

ft.app(target=main)

