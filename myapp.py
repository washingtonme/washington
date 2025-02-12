from flet import *

from custom_checkbox import CustomCheckBox


def main(page: Page):
    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"

    circle = Stack(
        controls=[
            Container(width=100, height=100, border_radius=50, bgcolor="white12"),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=["#00000000", PINK],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(
                    alignment="center",
                    controls=[
                        Container(
                            padding=padding.all(5),
                            bgcolor=BG,
                            width=90,
                            height=90,
                            border_radius=50,
                            content=Container(
                                bgcolor=FG,
                                height=80,
                                width=80,
                                border_radius=40,
                                content=Image(
                                    opacity=0.8,
                                    src="\Images/Adiado.jpeg",
                                ),
                            ),
                        )
                    ],
                ),
            ),
        ]
    )

    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right
        )
        page_2.controls[0].border_radius = border_radius.only(
            top_left=35, top_right=0, bottom_left=35, bottom_right=0
        )
        page_2.update()

    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 35
        page_2.controls[0].scale = transform.Scale(1, alignment=alignment.center_right)
        page_2.update()



    tasks = Column(
        height=400,
        scroll="auto",
    )

    tasks.controls.append(
        Container(
            height=70,
            width=400,
            bgcolor=BG,
            border_radius=25,
            padding=padding.only(left=20, top=25),
        )
    )


    def create_category_card(category_name, task_count, color):
        """
        Function to create a category card.
        """
        return Container( 
            border_radius=20,
            bgcolor=BG,
            width=170,
            height=110,
            padding=15,
            content=Column(
              controls=[
                Text(f"{task_count} Task(s)", size=12, color="white"),
                Text(category_name, size=16, weight="bold", color=color),
                Container(
                    width=160,
                    height=5,
                    bgcolor="white12",
                    border_radius=20,
                    content=Container(
                        bgcolor=color,
                    ),
                ),
            ]
        ),
    )


    categories_card = Row(scroll="auto")


    categories_card.controls.extend(
      [
        create_category_card("Smart Home App", 1, PINK),
        create_category_card("Prototype", 2, "#FFA726"),  
        create_category_card("Smart Lightpole", 1, "#66BB6A"), 
      ]
    )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment="spaceBetween",
                    controls=[
                        Container(
                            on_click=lambda e: shrink(e), content=Icon(icons.MENU)
                        ),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED),
                            ],
                        ),
                    ],
                ),
                Container(height=20),
                Text(value="What's up, Adiado!"),
                Text(value="COMPLETED PROJECTS"),
                Container(
                    padding=padding.only(
                        top=10,
                        bottom=20,
                    ),
                    content=categories_card,
                ),
                Container(height=20),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            bottom=2,
                            right=20,
                            icon=icons.ADD,
                            on_click=lambda _: page.go("/create_task"),
                        ),
                    ]
                ),
                
            ],
        ),
    )

    def create_task_view(page):
      new_task_name = TextField(
        label="Task Name",
        width=300,
        autofocus=True,
        hint_text="Enter task name (e.g., 'Complete project')",
      )
      category_dropdown = Dropdown(
        label="Category",
        width=300,
        options=[
            dropdown.Option("Work"),
            dropdown.Option("Studies"),
            dropdown.Option("Personal"),
        ],
        value="Business", 
    )
      time_input = TextField(
         label="Time (e.g., 3:00 PM)",
         width=300,
         hint_text="Enter time for the task",
        )

      def add_task(e):
        task_name = new_task_name.value.strip()
        category = category_dropdown.value
        time = time_input.value.strip()
        if task_name and time:
            # Add the new task to the `tasks` container
            tasks.controls.append(
                Container(
                    height=70,
                    width=400,
                    bgcolor=BG,
                    border_radius=25,
                    padding=padding.only(left=20, top=25),
                    content=CustomCheckBox(color=PINK, label=f"{task_name} ({category})at {time}"),
                )
            )

            new_task_name.value = ""
            time_input.value = ""
            category_dropdown.value = "Business"  # Reset to default value
            page.update()
            page.go("/")  # Navigate back to the main page

      return View(
        "/create_task",
        controls=[
            Container(
                bgcolor=FG,
                width=400,
                height=820,
                border_radius=35,
                padding=padding.all(20),
                content=Column(
                    controls=[
                        Row(
                            alignment="spaceBetween",
                            controls=[
                                IconButton(
                                    icon=icons.ARROW_BACK,
                                    on_click=lambda _: page.go("/"),
                                ),
                                Text("Create New Task", size=24, weight="bold"),
                            ],
                        ),
                        Container(height=20),
                        new_task_name,
                        category_dropdown,
                        time_input,
                        Container(
                            alignment=alignment.center,
                            margin=margin.only(top=20),
                            content=ElevatedButton(
                                text="Add Task",
                                icon=icons.ADD,
                                on_click=add_task,
                            ),
                        ),
                    ],
                ),
            )
        ],
    )


    

    page_1 = Container(
        # width=400,
        # height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),
        content=Column(
            controls=[
                Row(
                    alignment="end",
                    controls=[
                        Container(
                            border_radius=25,
                            padding=padding.only(
                                top=13,
                                left=13,
                            ),
                            # height=50,
                            # width=50,
                            border=border.all(color="white", width=1),
                            on_click=lambda e: restore(e),
                            content=Text("<"),
                        )
                    ],
                ),
                Container(height=20),  # height=20
                circle,
                Text("Adiado\nWashington", size=25, weight="bold"),
                Container(height=25),
                Row(
                    controls=[
                        Icon(icons.FAVORITE_BORDER_SHARP, color="white60"),
                        Text(
                            "Self Progress",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.CARD_TRAVEL, color="white60"),
                        Text(
                            "Work Progress",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.CALCULATE_OUTLINED, color="white60"),
                        Text(
                            "Study Progress",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                
                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.ANALYTICS_OUTLINED, color="white60"),
                        Text(
                            "Analytics",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),

                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.ROCKET_OUTLINED, color="white60"),
                        Text(
                            "Projects",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),

                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.SETTINGS_OUTLINED, color="white60"),
                        Text(
                            "Settings",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
            
                Text(
                    "Good",
                    color=FG,
                    font_family="poppins",
                ),
                Text(
                    "Consistency",
                    size=22,
                ),
            ]
        ),
    )

    page_2 = Row(
        alignment="end",
        controls=[
            Container(
                width=400,
                height=820,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve="decelerate"),
                padding=padding.only(top=50, left=20, right=20, bottom=5),
                content=Column(controls=[first_page_contents]),
            )
        ],
    )

    container = Container(
        width=400,
        height=820,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2,
            ]
        ),
    )

    pages = {
        "/": View(
            "/",
            [
                container,
            ],
        ),
        "/create_task": create_task_view(page),     
            
    }

    def route_change(route):
        page.views.clear()
        new_view = pages[route.route]
        page.views.append(new_view)
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


app(target=main, assets_dir="assets")