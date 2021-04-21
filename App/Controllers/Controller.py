
class Controller:

    @staticmethod
    def clear_view(view) -> None:
        master_children = view.winfo_children()
        if len(master_children) > 0:
            for child in master_children:
                child.destroy()

