from fabric.api import lcd, local, task

from docs_meta import get_conf

@task
def make(target):
    with lcd(get_conf().build.paths.projectroot):
        if isinstance(target, list):
            target_str = make + ' '.join([target])
        elif isinstance(target, basestring):
            target_str = ' '.join(['make', target])

        local(target_str)
