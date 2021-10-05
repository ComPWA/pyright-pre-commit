import yaml


class _IncreasedIndent(yaml.Dumper):
    # pylint: disable=too-many-ancestors
    def increase_indent(self, flow=False, indentless=False):  # type: ignore
        return super().increase_indent(flow, False)

    def write_line_break(self, data=None):  # type: ignore
        """See https://stackoverflow.com/a/44284819."""
        super().write_line_break(data)
        if len(self.indents) == 1:
            super().write_line_break()

with open(".pre-commit-hooks.yaml", "r") as stream:
    config = yaml.load(stream, Loader=yaml.SafeLoader)
config[0]["minimum_pre_commit_version"] = "0"
with open(".pre-commit-hooks.yaml", "w") as stream:
    yaml.dump(
        config,
        stream,
        sort_keys=False,
        Dumper=_IncreasedIndent,
        default_flow_style=False,
    )
